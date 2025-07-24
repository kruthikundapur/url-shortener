from flask import Flask, request, jsonify, redirect
from datetime import datetime
from app.core import URLShortener

app = Flask(__name__)
shortener = URLShortener()

@app.route('/api/shorten', methods=['POST'])
def shorten():
    # Validate input
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
        
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({"error": "URL is required"}), 400
    
    url = data['url']
    if not isinstance(url, str) or not url.startswith(('http://', 'https://')):
        return jsonify({"error": "URL must start with http:// or https://"}), 400
    
    # Create short URL - PROPERLY FORMATTED
    try:
        code = shortener.shorten(url)
        return jsonify({
            "short_code": code,
            "short_url": f"http://{request.host}/{code}"  # Fixed dynamic URL
        }), 201
    except Exception as e:
        return jsonify({"error": f"Shortening failed: {str(e)}"}), 500

@app.route('/<code>')
def redirect_to_url(code):
    url_data = shortener.get_url(code)
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404
    
    url_data['clicks'] = url_data.get('clicks', 0) + 1
    url_data['last_accessed'] = datetime.now().isoformat()
    return redirect(url_data['url'])

@app.route('/api/stats/<code>')
def get_stats(code):
    url_data = shortener.get_url(code)
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404
    
    return jsonify({
        "original_url": url_data['url'],
        "short_code": code,
        "clicks": url_data.get('clicks', 0),
        "created_at": url_data.get('created_at'),
        "last_accessed": url_data.get('last_accessed', 'Never')
    })

def main():
    app.run()

if __name__ == '__main__':
    app.run(debug=True)
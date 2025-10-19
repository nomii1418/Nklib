import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

async def upload_file_to_cloudinary(file_content: bytes, filename: str, folder: str = "mechanical_library"):
    """
    Upload file to Cloudinary
    
    Args:
        file_content: Binary file content
        filename: Original filename
        folder: Cloudinary folder name
    
    Returns:
        dict: Upload result with URL and public_id
    """
    try:
        # Upload file
        result = cloudinary.uploader.upload(
            file_content,
            folder=folder,
            resource_type="auto",
            public_id=filename.rsplit('.', 1)[0],  # Use filename without extension
            overwrite=False,
            unique_filename=True
        )
        
        return {
            "url": result["secure_url"],
            "public_id": result["public_id"],
            "format": result.get("format"),
            "size": result.get("bytes"),
            "resource_type": result.get("resource_type")
        }
    except Exception as e:
        raise Exception(f"Cloudinary upload failed: {str(e)}")

async def delete_file_from_cloudinary(public_id: str):
    """
    Delete file from Cloudinary
    
    Args:
        public_id: Cloudinary public_id of the file
    
    Returns:
        dict: Deletion result
    """
    try:
        result = cloudinary.uploader.destroy(public_id, resource_type="auto")
        return result
    except Exception as e:
        raise Exception(f"Cloudinary deletion failed: {str(e)}")

def get_cloudinary_url(public_id: str, transformation: dict = None):
    """
    Get Cloudinary URL with optional transformations
    
    Args:
        public_id: Cloudinary public_id
        transformation: Optional transformation parameters
    
    Returns:
        str: Cloudinary URL
    """
    if transformation:
        return cloudinary.CloudinaryImage(public_id).build_url(**transformation)
    return cloudinary.CloudinaryImage(public_id).build_url()

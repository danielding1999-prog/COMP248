import numpy as np
import matplotlib.pyplot as plt
csv_path= r'./numpy_image/image_b.csv'

def read_csv_image(csv_path):
    """
    Read image data from CSV file using NumPy.
    
    Args:
        csv_path (str): Path to the CSV file
        
    Returns:
        numpy.ndarray: Image data as NumPy array
    """
    try:
        # Read CSV file into NumPy array
        image_data = np.loadtxt(csv_path, delimiter=',')
        
        # TODO: Print the shape of the image data
        # HINT: use the attribute that tells dimensions of the NumPy array
        # URL: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html
        print(f"Successfully loaded CSV file: {csv_path}")
        print(f"Data shape: {_____}")   
        
        
       
        # TODO: Print the data type of the image data
        # HINT: use the attribute that tells the type of elements inside array
        # URL: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.dtype.html
        print(f"Data type: {_____}")    
        
        
       
        # TODO: Print the minimum pixel value in the image data
        # HINT: use NumPy function to find the minimum
        # URL: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.min.html
        print(f"Min value: {_____(____)}")   


       
        # TODO: Print the maximum pixel value in the image data
        # HINT: use NumPy function to find the maximum
        # URL: https://numpy.org/doc/stable/reference/generated/numpy.ndarray.max.html
        print(f"Max value: {_____(____)}")   
       
        
                
        # TODO: Display first few values
        # HINT: Use slicing to select the first 5 rows and first 5 columns
        # URL: https://numpy.org/doc/stable/user/basics.indexing.html
        print(f"First 5x5 pixel values:")
        print(image_data[_____, _____])   
        
                       
        # Display the image
        plt.figure(figsize=(10, 8))
        
        # Check if it's a grayscale or color image based on shape
        if len(image_data.shape) == 2:
            # Grayscale image
            plt.imshow(image_data, cmap='gray')
            plt.title('Grayscale Image from CSV')
        else:
            # Try to reshape for color image
            # Assuming the CSV was flattened from a color image
            height = image_data.shape[0]
            width = image_data.shape[1] // 3  # Assuming RGB (3 channels)
            
            try:
                # Reshape to (height, width, 3) for RGB
                color_image = image_data.reshape(height, width, 3).astype(np.uint8)
                plt.imshow(color_image)
                plt.title('Color Image from CSV')
            except:
                # If reshape fails, display as grayscale
                plt.imshow(image_data, cmap='gray')
                plt.title('Image from CSV (displayed as grayscale)')
        
        plt.axis('off')
        plt.colorbar()
        plt.show()
        
        # Additional image statistics
        print(f"\nImage Statistics:")
        print(f"Mean pixel value: {np.mean(image_data):.2f}")
        print(f"Standard deviation: {np.std(image_data):.2f}")
        print(f"Total pixels: {image_data.size}")
        
        return image_data
              
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None
    
read_csv_image(csv_path)
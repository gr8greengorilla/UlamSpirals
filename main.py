from PIL import Image, ImageDraw, ImageOps
import math

'''
Good poster resolution for 18x24
IMAGE_SIZE = (20000, 26666)
'''

LINE_THICKNESS = 0
CIRCLE_RADIUS = 3
LINE_LENGTH = 5
IMAGE_SIZE = (10000, 10000)


# Returns true if x is a prime number.
def isPrime(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True


# Draw a circle of radius CircleRadius at position if count is prime.
def drawCircleIfPrime(count, position):
    if (isPrime(count)):
        draw.ellipse((position[0] - CIRCLE_RADIUS / 2, position[1] - CIRCLE_RADIUS / 2, position[0] + CIRCLE_RADIUS / 2,
                      position[1] + CIRCLE_RADIUS / 2), fill=0)


if __name__ == '__main__':

    # Create the image and draw the background
    image = Image.new('RGB', IMAGE_SIZE)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0) + image.size, fill=(255, 255, 255))

    # Set the position to be centered, and init all the other needed variables.
    position = (image.size[0]/2, image.size[1]/2)
    sideLength = 1
    movement = 1
    count = 0
    horizontal = True
    i = 0

    # While the image is not full
    while 0 < position[0] < image.size[0] or 0 < position[1] < image.size[1]:

        # If the trail has gone the correct sideLength, start moving perpendicular.
        # Every other time, reverse the direction of the movement and increase length by 1 to make a spiral
        if i >= sideLength:
            if not horizontal:
                movement *= -1
                sideLength += 1
            horizontal = not horizontal
            i = 0

        # Calculate ending position of the line
        if horizontal:
            newPosition = (position[0] + LINE_LENGTH * movement, position[1])
        else:
            newPosition = (position[0], position[1] - LINE_LENGTH * movement)

        # Draw the line from last position to the new position
        if LINE_THICKNESS != 0:
            draw.line(position + newPosition, fill=0, width=LINE_THICKNESS)

        # Draw a circle at the old position if it is a prime count.
        # Must be done after line is drawn so circle is drawn over line
        # (noticeable if line and circle are different colors).
        count += 1
        drawCircleIfPrime(count, position)

        # Update the position and increase the sideLength after drawing one line segment
        position = newPosition
        i += 1

    # Inverse image for aesthetics.
    image = ImageOps.invert(image)
    image.save('test.png')





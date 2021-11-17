from PIL import Image
import typing
from math import sqrt
from itertools import groupby
import math
import random
import os
import sys
#img = Image.open("Brain_of_Cthulhu.gif").convert("RGB")
image = typing.NewType('Image', "Image")
"""
print("--------------")
print("Color Options:")
print("All")
print("Natural")
print("Bricks")
print("Living Fire")
print("Ores")
print("Solid")
print("Wood")
print("--------------")
choice = input("What color palette would you like? ")
choice = choice.lower()
if choice == "all":
    file = open("TerrariaBlockColors.txt")
elif choice == "natural":
    file = open("TerrariaBlockColorsNaturalOnly.txt")
elif choice == "bricks":
    file = open("TerrariaBlockColorsOnlyBricks.txt")
elif choice == "living fire" or choice == "fire":
    file = open("TerrariaBlockColorsOnlyLivingFireBlocks.txt")
elif choice == "ores":
    file = open("TerrariaBlockColorsOresOnly.txt")
elif choice == "solid":
    file = open("TerrariaBlockColorsSolidBlocks.txt")
elif choice == "wood":
    file = open("TerrariaBlockColorsWoodOnly.txt")
else:
    print("Invalid choice")
    file = open("TerrariaBlockColors.txt")
"""

file = open("Text Files/TerrariaBlockColors.txt")

lines = file.readlines()
BlockCount = {}
Blocks = []
Colors1 = []

for i in lines:
    line = i.split("|")
    Blocks.append(line[0])
    Colors1.append(line[1])
Colors2 = []
for i in Colors1:
    line = i.split("\n")
    Colors2.append(line[0])
Colors = []
for i in Colors2:
    line = i.split("(")
    line = line[1].split(")")
    line = line[0]
    res = tuple(map(int, line.split(', ')))
    Colors.append(res)
def closest_color(color, list):
    r, g, b = color
    color_diffs = []
    for color in list:
        cr, cg, cb = color
        color_diff = sqrt(abs(r - cr)**2 + abs(g - cg)**2 + abs(b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]
def getBlocksOfColor():
    BlockList = []
    ColorList = []
    for i in range(len(ImgColors)):
        C = closest_color(ImgColors[i], Colors)
        num = Colors.index(C)
        if C not in ColorList:
            ColorList.append(C)
            if Blocks[num] not in BlockList:
                BlockList.append(Blocks[num])
            else:
                pass
        else:
            pass
    return BlockList
#print(wOfColor())
def update(string):
    letter = 1
    while letter <= len(string):
        new_string = string[0:letter]
        sys.stdout.write("\r")
        sys.stdout.write("{0}".format(new_string))
        sys.stdout.flush()
        letter += 1
def getClosestColor(color):
    c = closest_color(color, Colors)
    return c
def modifyPic(img):
    width, height = img.size
    for x in range(width):
        for y in range(height):
            current_color = img.getpixel((x,y))
            color = getClosestColor(current_color)
            img.putpixel((x,y),color)
            #cP = "\033[1;32;40m x,y: ({0},{1}), Color: {2}".format(x, y, color)
            #update(cP)
    return img
def createRowInstructions(img: "Image", row: int, path: "path"):
    width, height = img.size
    croppedRow1 = img.crop((0,row-1,width,row))
    """if row == 0:
        pass
    else:
        croppedRow2 = img.crop((0, 0, width, row))
        try:
            os.mkdir(path+"/rows/")
        except:
            pass
        rowPath = "{0}/rows/".format(path)
        croppedRow2.save(rowPath + "Row{0}.png".format(row))"""
    lineRGB = []
    for i in range(croppedRow1.size[0]):
        lineRGB.append(croppedRow1.getpixel((i,0)))
    Block_Numbers = []
    Block_Order = []
    Block_Order2 = []
    Color_Number = []
    Blocks2 = []
    #print(len(lineRGB))
    """

    """
    for i in lineRGB:
        Color_Number.append(Colors.index(i))
    for j in Color_Number:
        Block_Order.append(Blocks[j])
    Block_Order.append("Sail")
    BlockOrder3 = []
    for k, v in groupby(Block_Order):
        BlockOrder3.append(k)
    BlockOrder4 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    Block_Count = []
    Block_Order3 = []
    for i in range(len(Block_Order)):
        if Block_Order[i] == BlockOrder3[count1]:
            count3 += 1
        elif Block_Order[i] != BlockOrder3[count1]:
            count1 += 1
            count3 += 1
            Block_Count.append(count3)
            count3 = 0
        else:
            pass
    lst = Block_Order
    temp = set(lst)
    result = {}
    for i in temp:
        result[i] = lst.count(i)
    #print(result)
    Order = []
    for k, v in groupby(Block_Order):
        Order.append(len(list(v)))
    """
    if FullList == True:
        if "Colors" in Returns and "Blocks Pixel Art" in Returns:
            return lineRGB, Block_Order
        elif "Colors" in Returns:
            return lineRGB
        elif "Blocks Pixel Art" in Returns:
            return Block_Order
    elif FullList == False:
        return BlockOrder3, Order
    else:
        pass
    """
    """
    for j in range(len(Block_Order)):
        if j == 0:
            pass
        elif Block_Order[j] is not Block_Order[j-1] or j == len(Block_Order)-1:
            count += 1
            Block_Numbers.append(count)
            count = 0
        elif Block_Order[j] is Block_Order[j-1]:
            count += 1
    for j in range(len(Block_Order)):
        if j == 0:
            pass
        elif Block_Order[j] is not Block_Order[j - 1] or j == len(Block_Order) - 1:
            Blocks2.append(Block_Order[j-1])
        elif Block_Order[j] is Block_Order[j - 1]:
            pass
    """
    return BlockOrder3, Order


"""
scaleOpt = input("Scale the image? (Y/N)")
if scaleOpt.lower() == "y":
    scale = input("How much would you like to scale down by? ")

    width, height = img.size
    img = img.resize((math.floor(width/int(scale)),math.floor(height/int(scale))),resample=3)
else:
    pass
"""
from collections import OrderedDict


def createMaterialsFiles(path, blockcount):
    Materials = open(path + "/Materials.txt","w")
    BlockCount = blockcount
    BlockCount2 = {k: v for k, v in sorted(BlockCount.items(), key=lambda item: item[1])}
    BlockCount3 = OrderedDict(reversed(list(BlockCount2.items())))
    #print(BlockCount3.items())
    BlockCount4 = []
    for key, value in BlockCount3.items():
        BlockCount4.append((key, value))
    #print(BlockCount4)
    def Convert(tup, di):
        for a, b in tup:
            di.setdefault(a, []).append(b)
        return di
    dict = {}
    BlockCount5 = Convert(BlockCount4, dict)
    BlockCount6 = list(BlockCount5.values())
    #print(BlockCount6[0][0])
    values = []
    for i in BlockCount6:
        values.append(i[0])
    #print(values)

    BlockCountValues = values
    #print(BlockCountValues)
    BlockCountBlocks = list(BlockCount5.keys())
    #print(BlockCountBlocks)
    #print(BlockCount)
    for i in range(len(BlockCountBlocks)):
        Stacks = BlockCountValues[i] / 999
        FloorStacks = math.floor(Stacks)
        if type(Stacks) == float:
            Stacks = math.floor(Stacks)
            if Stacks < 0.1:
                Items = BlockCountValues[i] % 999
                Materials.write("Item: {0}, Items: {1}".format(BlockCountBlocks[i], Items))
            else:
                Items = BlockCountValues[i] % 999
                #print("Item: {0}, Stacks: {1}, Items: {2}".format(BlockCountBlocks[i], Stacks, Items))
                Materials.write("Item: {0}, Stacks: {1}, Items: {2}".format(BlockCountBlocks[i], Stacks, Items))
        else:
            #print("Item: {0}, Stacks: {1}".format(BlockCountBlocks[i], Stacks))
            Materials.write("Item: {0}, Stacks: {1}".format(BlockCountBlocks[i], Stacks))
        Materials.write("\n")
    Materials.close()



def createAll(file,saveTo,name):
    img = Image.open(file).convert("RGB")
    moddedImg = modifyPic(img)
    #moddedImg.show()
    width, height = moddedImg.size
    if os.path.isdir(saveTo):
        print("File Exists")
    else:
        file_names = saveTo.split("/")
        print(file_names)
        if os.path.isdir(file_names[0]):
            com_file_names1 = f"{file_names[0]}/{file_names[1]}"
            print(com_file_names1)
            if os.path.isdir(com_file_names1):
                com_file_names2 = f"{com_file_names1}/{file_names[2]}"
                print(com_file_names2)
        else:
            os.mkdir(f"{file_names[0]}")

    for j in range(height):
        Blocks2, Block0 = createRowInstructions(moddedImg, j, saveTo)
        #instructions = open(instructions_folder + " Instructions/Instruction_Row{0}.txt".format(j),"w")
        instructions = open(saveTo + "/Instruction_Row{0}.txt".format(j), "w")
        res = {}
        count2 = 0
        for i in Blocks2:
            if i in BlockCount.keys():
                pass
            else:
                BlockCount.update({i: 0})
        for j in range(len(Block0)):
            BlockCount[Blocks2[j]] = BlockCount[Blocks2[j]] + Block0[j]
            instructions.write("{0}: {1}".format(Block0[j], Blocks2[j]))
            instructions.write("\n")
        instructions.close()
    moddedImg.save(saveTo + "/{0} Pixel Art.png".format(name))
    createMaterialsFiles(saveTo, BlockCount)

"""
for key in Block0:
    for value in Blocks2:
        res[key] = value
        Blocks2.remove(value)
        break
"""
createAll("Brain of Cthulhu Second Form.png","Images Pixel Art/Bosses/Brain of Cthulhu/Brain of Cthulhu Second Form","")

#########################################
#   STOPPED ON Eye of cthulhu row 109   #
#########################################
# Stopped on row 20 on empress of light #
#########################################

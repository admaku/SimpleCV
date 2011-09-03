__version__ = '1.1.0'

from SimpleCV.base import *
from SimpleCV.Camera import *
from SimpleCV.Color import *
from SimpleCV.Detection import *   
from SimpleCV.Features import *
from SimpleCV.ImageClass import *
from SimpleCV.Stream import *
from SimpleCV.Font import *
from SimpleCV.ColorModel import *
from SimpleCV.DrawingLayer import *
from SimpleCV.BlobMaker import *
from SimpleCV.SegmentationBase import *
from SimpleCV.ColorSegmentation import *
from SimpleCV.DiffSegmentation import *
from SimpleCV.BOFFeatureExtractor import *
from SimpleCV.RunningSegmentation import *
from SimpleCV.CodebookSegmentation import *
from SimpleCV.FeatureExtractorBase import *
from SimpleCV.HueHistogramFeatureExtractor import *
from SimpleCV.EdgeHistogramFeatureExtractor import *
if (__name__ == '__main__'):
    from SimpleCV.Shell import *
    main()

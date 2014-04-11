//
//  ViewController.h
//  Scanner
//
//  Created by Jacky Shen on 14-4-11.
//  Copyright (c) 2014年 JackyShen. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "ZBarSDK.h"

@interface ViewController : UIViewController<ZBarReaderDelegate>

@property (nonatomic) IBOutlet UIImageView *resultImage;
@property (nonatomic) IBOutlet UILabel *resultText;


- (IBAction) scanButtonTapped;

@end

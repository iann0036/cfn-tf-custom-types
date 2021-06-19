# TF::AWS::ElasticBeanstalkApplication AppversionLifecycleDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#deletesourcefroms3" title="DeleteSourceFromS3">DeleteSourceFromS3</a>" : <i>Boolean</i>,
    "<a href="#maxageindays" title="MaxAgeInDays">MaxAgeInDays</a>" : <i>Double</i>,
    "<a href="#maxcount" title="MaxCount">MaxCount</a>" : <i>Double</i>,
    "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#deletesourcefroms3" title="DeleteSourceFromS3">DeleteSourceFromS3</a>: <i>Boolean</i>
<a href="#maxageindays" title="MaxAgeInDays">MaxAgeInDays</a>: <i>Double</i>
<a href="#maxcount" title="MaxCount">MaxCount</a>: <i>Double</i>
<a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
</pre>

## Properties

#### DeleteSourceFromS3

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAgeInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


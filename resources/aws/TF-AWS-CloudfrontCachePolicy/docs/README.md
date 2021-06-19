# TF::AWS::CloudfrontCachePolicy

CloudFormation equivalent of aws_cloudfront_cache_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CloudfrontCachePolicy",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>" : <i>Double</i>,
        "<a href="#etag" title="Etag">Etag</a>" : <i>String</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
        "<a href="#minttl" title="MinTtl">MinTtl</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parametersincachekeyandforwardedtoorigin" title="ParametersInCacheKeyAndForwardedToOrigin">ParametersInCacheKeyAndForwardedToOrigin</a>" : <i>[ <a href="parametersincachekeyandforwardedtoorigindefinition.md">ParametersInCacheKeyAndForwardedToOriginDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CloudfrontCachePolicy
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#defaultttl" title="DefaultTtl">DefaultTtl</a>: <i>Double</i>
    <a href="#etag" title="Etag">Etag</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
    <a href="#minttl" title="MinTtl">MinTtl</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parametersincachekeyandforwardedtoorigin" title="ParametersInCacheKeyAndForwardedToOrigin">ParametersInCacheKeyAndForwardedToOrigin</a>: <i>
      - <a href="parametersincachekeyandforwardedtoorigindefinition.md">ParametersInCacheKeyAndForwardedToOriginDefinition</a></i>
</pre>

## Properties

#### Comment

A comment to describe the cache policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultTtl

The default amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Etag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

The maximum amount of time, in seconds, that objects stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinTtl

The minimum amount of time, in seconds, that you want objects to stay in the CloudFront cache before CloudFront sends another request to the origin to see if the object has been updated.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify the cache policy.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParametersInCacheKeyAndForwardedToOrigin

_Required_: No

_Type_: List of <a href="parametersincachekeyandforwardedtoorigindefinition.md">ParametersInCacheKeyAndForwardedToOriginDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


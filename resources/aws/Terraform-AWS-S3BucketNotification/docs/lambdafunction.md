# Terraform::AWS::S3BucketNotification LambdaFunction

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#events" title="Events">Events</a>" : <i>[ String, ... ]</i>,
    "<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>" : <i>String</i>,
    "<a href="#filtersuffix" title="FilterSuffix">FilterSuffix</a>" : <i>String</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#lambdafunctionarn" title="LambdaFunctionArn">LambdaFunctionArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#events" title="Events">Events</a>: <i>
      - String</i>
<a href="#filterprefix" title="FilterPrefix">FilterPrefix</a>: <i>String</i>
<a href="#filtersuffix" title="FilterSuffix">FilterSuffix</a>: <i>String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#lambdafunctionarn" title="LambdaFunctionArn">LambdaFunctionArn</a>: <i>String</i>
</pre>

## Properties

#### Events

_Required_: Yes
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterPrefix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FilterSuffix

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaFunctionArn

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


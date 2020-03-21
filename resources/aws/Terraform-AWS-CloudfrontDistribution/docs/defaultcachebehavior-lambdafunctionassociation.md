# Terraform::AWS::CloudfrontDistribution DefaultCacheBehavior LambdaFunctionAssociation

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#eventtype" title="EventType">EventType</a>" : <i>String</i>,
    "<a href="#includebody" title="IncludeBody">IncludeBody</a>" : <i>Boolean</i>,
    "<a href="#lambdaarn" title="LambdaArn">LambdaArn</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#eventtype" title="EventType">EventType</a>: <i>String</i>
<a href="#includebody" title="IncludeBody">IncludeBody</a>: <i>Boolean</i>
<a href="#lambdaarn" title="LambdaArn">LambdaArn</a>: <i>String</i>
</pre>

## Properties

#### EventType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludeBody

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LambdaArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


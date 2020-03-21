# Terraform::AWS::SagemakerEndpointConfiguration ProductionVariants

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acceleratortype" title="AcceleratorType">AcceleratorType</a>" : <i>String</i>,
    "<a href="#initialinstancecount" title="InitialInstanceCount">InitialInstanceCount</a>" : <i>Double</i>,
    "<a href="#initialvariantweight" title="InitialVariantWeight">InitialVariantWeight</a>" : <i>Double</i>,
    "<a href="#instancetype" title="InstanceType">InstanceType</a>" : <i>String</i>,
    "<a href="#modelname" title="ModelName">ModelName</a>" : <i>String</i>,
    "<a href="#variantname" title="VariantName">VariantName</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acceleratortype" title="AcceleratorType">AcceleratorType</a>: <i>String</i>
<a href="#initialinstancecount" title="InitialInstanceCount">InitialInstanceCount</a>: <i>Double</i>
<a href="#initialvariantweight" title="InitialVariantWeight">InitialVariantWeight</a>: <i>Double</i>
<a href="#instancetype" title="InstanceType">InstanceType</a>: <i>String</i>
<a href="#modelname" title="ModelName">ModelName</a>: <i>String</i>
<a href="#variantname" title="VariantName">VariantName</a>: <i>String</i>
</pre>

## Properties

#### AcceleratorType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialInstanceCount

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InitialVariantWeight

_Required_: No
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModelName

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VariantName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


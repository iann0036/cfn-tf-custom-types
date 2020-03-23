# Terraform::AWS::SagemakerNotebookInstanceLifecycleConfiguration

Provides a lifecycle configuration for SageMaker Notebook Instances.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SagemakerNotebookInstanceLifecycleConfiguration",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#oncreate" title="OnCreate">OnCreate</a>" : <i>String</i>,
        "<a href="#onstart" title="OnStart">OnStart</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SagemakerNotebookInstanceLifecycleConfiguration
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#oncreate" title="OnCreate">OnCreate</a>: <i>String</i>
    <a href="#onstart" title="OnStart">OnStart</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the lifecycle configuration (must be unique). If omitted, Terraform will assign a random, unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnCreate

A shell script (base64-encoded) that runs only once when the SageMaker Notebook Instance is created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnStart

A shell script (base64-encoded) that runs every time the SageMaker Notebook Instance is started including the time it's created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.


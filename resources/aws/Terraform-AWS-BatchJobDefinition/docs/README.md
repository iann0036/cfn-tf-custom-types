# Terraform::AWS::BatchJobDefinition

Provides a Batch Job Definition resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::BatchJobDefinition",
    "Properties" : {
        "<a href="#containerproperties" title="ContainerProperties">ContainerProperties</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#parameters" title="Parameters">Parameters</a>" : <i>[ <a href="parameters.md">Parameters</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#retrystrategy" title="RetryStrategy">RetryStrategy</a>" : <i>[ <a href="retrystrategy.md">RetryStrategy</a>, ... ]</i>,
        "<a href="#timeout" title="Timeout">Timeout</a>" : <i>[ <a href="timeout.md">Timeout</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::BatchJobDefinition
Properties:
    <a href="#containerproperties" title="ContainerProperties">ContainerProperties</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#parameters" title="Parameters">Parameters</a>: <i>
      - <a href="parameters.md">Parameters</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#retrystrategy" title="RetryStrategy">RetryStrategy</a>: <i>
      - <a href="retrystrategy.md">RetryStrategy</a></i>
    <a href="#timeout" title="Timeout">Timeout</a>: <i>
      - <a href="timeout.md">Timeout</a></i>
</pre>

## Properties

#### ContainerProperties

A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Specifies the name of the job definition.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parameters

Specifies the parameter substitution placeholders to set in the job definition.

_Required_: No

_Type_: List of <a href="parameters.md">Parameters</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of job definition.  Must be `container`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetryStrategy

_Required_: No

_Type_: List of <a href="retrystrategy.md">RetryStrategy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: No

_Type_: List of <a href="timeout.md">Timeout</a>

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

#### Revision

Returns the <code>Revision</code> value.


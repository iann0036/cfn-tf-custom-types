# Terraform::AWS::SagemakerModel

Provides a SageMaker model resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::SagemakerModel",
    "Properties" : {
        "<a href="#enablenetworkisolation" title="EnableNetworkIsolation">EnableNetworkIsolation</a>" : <i>Boolean</i>,
        "<a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#container" title="Container">Container</a>" : <i>[ <a href="container.md">Container</a>, ... ]</i>,
        "<a href="#primarycontainer" title="PrimaryContainer">PrimaryContainer</a>" : <i>[ <a href="primarycontainer.md">PrimaryContainer</a>, ... ]</i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ <a href="vpcconfig.md">VpcConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::SagemakerModel
Properties:
    <a href="#enablenetworkisolation" title="EnableNetworkIsolation">EnableNetworkIsolation</a>: <i>Boolean</i>
    <a href="#executionrolearn" title="ExecutionRoleArn">ExecutionRoleArn</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#container" title="Container">Container</a>: <i>
      - <a href="container.md">Container</a></i>
    <a href="#primarycontainer" title="PrimaryContainer">PrimaryContainer</a>: <i>
      - <a href="primarycontainer.md">PrimaryContainer</a></i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - <a href="vpcconfig.md">VpcConfig</a></i>
</pre>

## Properties

#### EnableNetworkIsolation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExecutionRoleArn

A role that SageMaker can assume to access model artifacts and docker images for deployment.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the model (must be unique). If omitted, Terraform will assign a random, unique name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Container

_Required_: No

_Type_: List of <a href="container.md">Container</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrimaryContainer

_Required_: No

_Type_: List of <a href="primarycontainer.md">PrimaryContainer</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of <a href="vpcconfig.md">VpcConfig</a>

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


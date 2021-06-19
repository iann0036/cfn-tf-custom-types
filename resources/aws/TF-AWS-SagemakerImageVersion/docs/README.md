# TF::AWS::SagemakerImageVersion

Provides a Sagemaker Image Version resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SagemakerImageVersion",
    "Properties" : {
        "<a href="#baseimage" title="BaseImage">BaseImage</a>" : <i>String</i>,
        "<a href="#imagename" title="ImageName">ImageName</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SagemakerImageVersion
Properties:
    <a href="#baseimage" title="BaseImage">BaseImage</a>: <i>String</i>
    <a href="#imagename" title="ImageName">ImageName</a>: <i>String</i>
</pre>

## Properties

#### BaseImage

The registry path of the container image on which this image version is based.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImageName

The name of the image. Must be unique to your account.

_Required_: Yes

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

#### ContainerImage

Returns the <code>ContainerImage</code> value.

#### Id

Returns the <code>Id</code> value.

#### ImageArn

Returns the <code>ImageArn</code> value.

#### Version

Returns the <code>Version</code> value.


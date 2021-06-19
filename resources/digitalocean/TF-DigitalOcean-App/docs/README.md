# TF::DigitalOcean::App

Provides a DigitalOcean App resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::DigitalOcean::App",
    "Properties" : {
        "<a href="#spec" title="Spec">Spec</a>" : <i>[ <a href="specdefinition.md">SpecDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::DigitalOcean::App
Properties:
    <a href="#spec" title="Spec">Spec</a>: <i>
      - <a href="specdefinition.md">SpecDefinition</a></i>
</pre>

## Properties

#### Spec

_Required_: No

_Type_: List of <a href="specdefinition.md">SpecDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ActiveDeploymentId

Returns the <code>ActiveDeploymentId</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### DefaultIngress

Returns the <code>DefaultIngress</code> value.

#### Id

Returns the <code>Id</code> value.

#### LiveUrl

Returns the <code>LiveUrl</code> value.

#### UpdatedAt

Returns the <code>UpdatedAt</code> value.


# TF::KubernetesAlpha::KubernetesManifest

CloudFormation equivalent of kubernetes_manifest

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::KubernetesAlpha::KubernetesManifest",
    "Properties" : {
        "<a href="#manifest" title="Manifest">Manifest</a>" : <i>String</i>,
        "<a href="#object" title="Object">Object</a>" : <i>String</i>,
        "<a href="#waitfor" title="WaitFor">WaitFor</a>" : <i><a href="waitfordefinition2.md">WaitForDefinition2</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::KubernetesAlpha::KubernetesManifest
Properties:
    <a href="#manifest" title="Manifest">Manifest</a>: <i>String</i>
    <a href="#object" title="Object">Object</a>: <i>String</i>
    <a href="#waitfor" title="WaitFor">WaitFor</a>: <i><a href="waitfordefinition2.md">WaitForDefinition2</a></i>
</pre>

## Properties

#### Manifest

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Object

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitFor

_Required_: No

_Type_: <a href="waitfordefinition2.md">WaitForDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.


# TF::Rancher2::Secret

CloudFormation equivalent of rancher2_secret

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Rancher2::Secret",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#data" title="Data">Data</a>" : <i>[ <a href="datadefinition.md">DataDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>String</i>,
        "<a href="#projectid" title="ProjectId">ProjectId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Rancher2::Secret
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#data" title="Data">Data</a>: <i>
      - <a href="datadefinition.md">DataDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>String</i>
    <a href="#projectid" title="ProjectId">ProjectId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Data

_Required_: Yes

_Type_: List of <a href="datadefinition.md">DataDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

# TF::Volterra::NetworkConnector

CloudFormation equivalent of volterra_network_connector

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::NetworkConnector",
    "Properties" : {
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#disableforwardproxy" title="DisableForwardProxy">DisableForwardProxy</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#slitoslodr" title="SliToSloDr">SliToSloDr</a>" : <i>Boolean</i>,
        "<a href="#enableforwardproxy" title="EnableForwardProxy">EnableForwardProxy</a>" : <i>[ <a href="enableforwardproxydefinition.md">EnableForwardProxyDefinition</a>, ... ]</i>,
        "<a href="#slitoglobaldr" title="SliToGlobalDr">SliToGlobalDr</a>" : <i>[ <a href="slitoglobaldrdefinition.md">SliToGlobalDrDefinition</a>, ... ]</i>,
        "<a href="#slitoglobalsnat" title="SliToGlobalSnat">SliToGlobalSnat</a>" : <i>[ <a href="slitoglobalsnatdefinition.md">SliToGlobalSnatDefinition</a>, ... ]</i>,
        "<a href="#slitoslosnat" title="SliToSloSnat">SliToSloSnat</a>" : <i>[ <a href="slitoslosnatdefinition.md">SliToSloSnatDefinition</a>, ... ]</i>,
        "<a href="#slotoglobaldr" title="SloToGlobalDr">SloToGlobalDr</a>" : <i>[ <a href="slotoglobaldrdefinition.md">SloToGlobalDrDefinition</a>, ... ]</i>,
        "<a href="#slotoglobalsnat" title="SloToGlobalSnat">SloToGlobalSnat</a>" : <i>[ <a href="slotoglobalsnatdefinition.md">SloToGlobalSnatDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::NetworkConnector
Properties:
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#disableforwardproxy" title="DisableForwardProxy">DisableForwardProxy</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#slitoslodr" title="SliToSloDr">SliToSloDr</a>: <i>Boolean</i>
    <a href="#enableforwardproxy" title="EnableForwardProxy">EnableForwardProxy</a>: <i>
      - <a href="enableforwardproxydefinition.md">EnableForwardProxyDefinition</a></i>
    <a href="#slitoglobaldr" title="SliToGlobalDr">SliToGlobalDr</a>: <i>
      - <a href="slitoglobaldrdefinition.md">SliToGlobalDrDefinition</a></i>
    <a href="#slitoglobalsnat" title="SliToGlobalSnat">SliToGlobalSnat</a>: <i>
      - <a href="slitoglobalsnatdefinition.md">SliToGlobalSnatDefinition</a></i>
    <a href="#slitoslosnat" title="SliToSloSnat">SliToSloSnat</a>: <i>
      - <a href="slitoslosnatdefinition.md">SliToSloSnatDefinition</a></i>
    <a href="#slotoglobaldr" title="SloToGlobalDr">SloToGlobalDr</a>: <i>
      - <a href="slotoglobaldrdefinition.md">SloToGlobalDrDefinition</a></i>
    <a href="#slotoglobalsnat" title="SloToGlobalSnat">SloToGlobalSnat</a>: <i>
      - <a href="slotoglobalsnatdefinition.md">SloToGlobalSnatDefinition</a></i>
</pre>

## Properties

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableForwardProxy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of <a href="labelsdefinition.md">LabelsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Namespace

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SliToSloDr

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableForwardProxy

_Required_: No

_Type_: List of <a href="enableforwardproxydefinition.md">EnableForwardProxyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SliToGlobalDr

_Required_: No

_Type_: List of <a href="slitoglobaldrdefinition.md">SliToGlobalDrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SliToGlobalSnat

_Required_: No

_Type_: List of <a href="slitoglobalsnatdefinition.md">SliToGlobalSnatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SliToSloSnat

_Required_: No

_Type_: List of <a href="slitoslosnatdefinition.md">SliToSloSnatDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SloToGlobalDr

_Required_: No

_Type_: List of <a href="slotoglobaldrdefinition.md">SloToGlobalDrDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SloToGlobalSnat

_Required_: No

_Type_: List of <a href="slotoglobalsnatdefinition.md">SloToGlobalSnatDefinition</a>

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


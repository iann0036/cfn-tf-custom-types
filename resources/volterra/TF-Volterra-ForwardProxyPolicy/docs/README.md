# TF::Volterra::ForwardProxyPolicy

CloudFormation equivalent of volterra_forward_proxy_policy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::ForwardProxyPolicy",
    "Properties" : {
        "<a href="#allowall" title="AllowAll">AllowAll</a>" : <i>Boolean</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#anyproxy" title="AnyProxy">AnyProxy</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#drphttpconnect" title="DrpHttpConnect">DrpHttpConnect</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#allowlist" title="AllowList">AllowList</a>" : <i>[ <a href="allowlistdefinition.md">AllowListDefinition</a>, ... ]</i>,
        "<a href="#denylist" title="DenyList">DenyList</a>" : <i>[ <a href="denylistdefinition.md">DenyListDefinition</a>, ... ]</i>,
        "<a href="#networkconnector" title="NetworkConnector">NetworkConnector</a>" : <i>[ <a href="networkconnectordefinition.md">NetworkConnectorDefinition</a>, ... ]</i>,
        "<a href="#proxylabelselector" title="ProxyLabelSelector">ProxyLabelSelector</a>" : <i>[ <a href="proxylabelselectordefinition.md">ProxyLabelSelectorDefinition</a>, ... ]</i>,
        "<a href="#rulelist" title="RuleList">RuleList</a>" : <i>[ <a href="rulelistdefinition.md">RuleListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::ForwardProxyPolicy
Properties:
    <a href="#allowall" title="AllowAll">AllowAll</a>: <i>Boolean</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#anyproxy" title="AnyProxy">AnyProxy</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#drphttpconnect" title="DrpHttpConnect">DrpHttpConnect</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#allowlist" title="AllowList">AllowList</a>: <i>
      - <a href="allowlistdefinition.md">AllowListDefinition</a></i>
    <a href="#denylist" title="DenyList">DenyList</a>: <i>
      - <a href="denylistdefinition.md">DenyListDefinition</a></i>
    <a href="#networkconnector" title="NetworkConnector">NetworkConnector</a>: <i>
      - <a href="networkconnectordefinition.md">NetworkConnectorDefinition</a></i>
    <a href="#proxylabelselector" title="ProxyLabelSelector">ProxyLabelSelector</a>: <i>
      - <a href="proxylabelselectordefinition.md">ProxyLabelSelectorDefinition</a></i>
    <a href="#rulelist" title="RuleList">RuleList</a>: <i>
      - <a href="rulelistdefinition.md">RuleListDefinition</a></i>
</pre>

## Properties

#### AllowAll

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Annotations

_Required_: No

_Type_: List of <a href="annotationsdefinition.md">AnnotationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AnyProxy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Disable

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DrpHttpConnect

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

#### AllowList

_Required_: No

_Type_: List of <a href="allowlistdefinition.md">AllowListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DenyList

_Required_: No

_Type_: List of <a href="denylistdefinition.md">DenyListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConnector

_Required_: No

_Type_: List of <a href="networkconnectordefinition.md">NetworkConnectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProxyLabelSelector

_Required_: No

_Type_: List of <a href="proxylabelselectordefinition.md">ProxyLabelSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleList

_Required_: No

_Type_: List of <a href="rulelistdefinition.md">RuleListDefinition</a>

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


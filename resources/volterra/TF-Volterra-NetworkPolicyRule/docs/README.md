# TF::Volterra::NetworkPolicyRule

CloudFormation equivalent of volterra_network_policy_rule

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Volterra::NetworkPolicyRule",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#annotations" title="Annotations">Annotations</a>" : <i>[ <a href="annotationsdefinition.md">AnnotationsDefinition</a>, ... ]</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#disable" title="Disable">Disable</a>" : <i>Boolean</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ <a href="labelsdefinition.md">LabelsDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespace" title="Namespace">Namespace</a>" : <i>String</i>,
        "<a href="#ports" title="Ports">Ports</a>" : <i>[ String, ... ]</i>,
        "<a href="#protocol" title="Protocol">Protocol</a>" : <i>String</i>,
        "<a href="#advancedaction" title="AdvancedAction">AdvancedAction</a>" : <i>[ <a href="advancedactiondefinition.md">AdvancedActionDefinition</a>, ... ]</i>,
        "<a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>" : <i>[ <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>, ... ]</i>,
        "<a href="#labelmatcher" title="LabelMatcher">LabelMatcher</a>" : <i>[ <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a>, ... ]</i>,
        "<a href="#prefix" title="Prefix">Prefix</a>" : <i>[ <a href="prefixdefinition.md">PrefixDefinition</a>, ... ]</i>,
        "<a href="#prefixselector" title="PrefixSelector">PrefixSelector</a>" : <i>[ <a href="prefixselectordefinition.md">PrefixSelectorDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Volterra::NetworkPolicyRule
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#annotations" title="Annotations">Annotations</a>: <i>
      - <a href="annotationsdefinition.md">AnnotationsDefinition</a></i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#disable" title="Disable">Disable</a>: <i>Boolean</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - <a href="labelsdefinition.md">LabelsDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespace" title="Namespace">Namespace</a>: <i>String</i>
    <a href="#ports" title="Ports">Ports</a>: <i>
      - String</i>
    <a href="#protocol" title="Protocol">Protocol</a>: <i>String</i>
    <a href="#advancedaction" title="AdvancedAction">AdvancedAction</a>: <i>
      - <a href="advancedactiondefinition.md">AdvancedActionDefinition</a></i>
    <a href="#ipprefixset" title="IpPrefixSet">IpPrefixSet</a>: <i>
      - <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a></i>
    <a href="#labelmatcher" title="LabelMatcher">LabelMatcher</a>: <i>
      - <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a></i>
    <a href="#prefix" title="Prefix">Prefix</a>: <i>
      - <a href="prefixdefinition.md">PrefixDefinition</a></i>
    <a href="#prefixselector" title="PrefixSelector">PrefixSelector</a>: <i>
      - <a href="prefixselectordefinition.md">PrefixSelectorDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

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

#### Ports

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Protocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdvancedAction

_Required_: No

_Type_: List of <a href="advancedactiondefinition.md">AdvancedActionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpPrefixSet

_Required_: No

_Type_: List of <a href="ipprefixsetdefinition.md">IpPrefixSetDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LabelMatcher

_Required_: No

_Type_: List of <a href="labelmatcherdefinition.md">LabelMatcherDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

_Required_: No

_Type_: List of <a href="prefixdefinition.md">PrefixDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixSelector

_Required_: No

_Type_: List of <a href="prefixselectordefinition.md">PrefixSelectorDefinition</a>

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


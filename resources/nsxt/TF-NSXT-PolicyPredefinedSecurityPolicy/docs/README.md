# TF::NSXT::PolicyPredefinedSecurityPolicy

This resource provides a method to modify default Security Policy and its rules.
This can be default layer2 policy or default layer3 policy. Maximum one resource
for each type should exist in your configuration.

~> **NOTE:** An absolute path, such as `/infra/domains/default/security-policies/default-layer3-section`, can be provided for this resource (this approach will work slightly faster, as the roundtrip for data source retrieval will be spared) In the example below a data source is used in order to pull the predefined policy.

This resource is applicable to NSX Global Manager, NSX Policy Manager and VMC.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NSXT::PolicyPredefinedSecurityPolicy",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#defaultrule" title="DefaultRule">DefaultRule</a>" : <i>[ <a href="defaultruledefinition.md">DefaultRuleDefinition</a>, ... ]</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#tag" title="Tag">Tag</a>" : <i>[ <a href="tagdefinition.md">TagDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NSXT::PolicyPredefinedSecurityPolicy
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#defaultrule" title="DefaultRule">DefaultRule</a>: <i>
      - <a href="defaultruledefinition.md">DefaultRuleDefinition</a></i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#tag" title="Tag">Tag</a>: <i>
      - <a href="tagdefinition.md">TagDefinition</a></i>
</pre>

## Properties

#### Description

Description of the resource.
* `logged` - (Optional) A boolean flag to enable packet logging.
* `log_label` - (Optional) Additional information (string) which will be propagated to the rule syslog.
* `tag` - (Optional) A list of scope + tag pairs to associate with this Rule.
* `action` - (Optional) The action for the Rule. Must be one of: `ALLOW`, `DROP` or `REJECT`. Note that `REJECT` action is not applicable for L2 policy.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

Policy path for the predefined Security Policy to modify.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultRule

_Required_: No

_Type_: List of <a href="defaultruledefinition.md">DefaultRuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tag

_Required_: No

_Type_: List of <a href="tagdefinition.md">TagDefinition</a>

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

#### Revision

Returns the <code>Revision</code> value.


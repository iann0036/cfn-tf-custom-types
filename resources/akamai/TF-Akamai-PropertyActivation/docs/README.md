# TF::Akamai::PropertyActivation

~> **Note** Version 1.0.0 of the Akamai Terraform Provider is now available for the Provisioning module. To upgrade to this version, you have to update this resource. See the [migration guide](../guides/1.0_migration.md) for details.

The `akamai_property_activation` resource lets you activate a property version. An activation deploys the version to either the Akamai staging or production network. You can activate a specific version multiple times if you need to.  

Before activating on production, activate on staging first. This way you can detect any problems in staging before your changes progress to production.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::PropertyActivation",
    "Properties" : {
        "<a href="#activationid" title="ActivationId">ActivationId</a>" : <i>String</i>,
        "<a href="#autoacknowledgerulewarnings" title="AutoAcknowledgeRuleWarnings">AutoAcknowledgeRuleWarnings</a>" : <i>Boolean</i>,
        "<a href="#contact" title="Contact">Contact</a>" : <i>[ String, ... ]</i>,
        "<a href="#network" title="Network">Network</a>" : <i>String</i>,
        "<a href="#property" title="Property">Property</a>" : <i>String</i>,
        "<a href="#propertyid" title="PropertyId">PropertyId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>Double</i>,
        "<a href="#ruleerrors" title="RuleErrors">RuleErrors</a>" : <i>[ <a href="ruleerrorsdefinition.md">RuleErrorsDefinition</a>, ... ]</i>,
        "<a href="#rulewarnings" title="RuleWarnings">RuleWarnings</a>" : <i>[ <a href="rulewarningsdefinition.md">RuleWarningsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::PropertyActivation
Properties:
    <a href="#activationid" title="ActivationId">ActivationId</a>: <i>String</i>
    <a href="#autoacknowledgerulewarnings" title="AutoAcknowledgeRuleWarnings">AutoAcknowledgeRuleWarnings</a>: <i>Boolean</i>
    <a href="#contact" title="Contact">Contact</a>: <i>
      - String</i>
    <a href="#network" title="Network">Network</a>: <i>String</i>
    <a href="#property" title="Property">Property</a>: <i>String</i>
    <a href="#propertyid" title="PropertyId">PropertyId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>Double</i>
    <a href="#ruleerrors" title="RuleErrors">RuleErrors</a>: <i>
      - <a href="ruleerrorsdefinition.md">RuleErrorsDefinition</a></i>
    <a href="#rulewarnings" title="RuleWarnings">RuleWarnings</a>: <i>
      - <a href="rulewarningsdefinition.md">RuleWarningsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ActivationId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutoAcknowledgeRuleWarnings

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Contact

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Network

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Property

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleErrors

_Required_: No

_Type_: List of <a href="ruleerrorsdefinition.md">RuleErrorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleWarnings

_Required_: No

_Type_: List of <a href="rulewarningsdefinition.md">RuleWarningsDefinition</a>

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

#### Errors

Returns the <code>Errors</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

#### Warnings

Returns the <code>Warnings</code> value.


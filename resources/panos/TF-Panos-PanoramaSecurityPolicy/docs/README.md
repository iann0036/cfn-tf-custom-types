# TF::Panos::PanoramaSecurityPolicy

This resource allows you to manage the full security posture.

-> **Note:** `panos_panorama_security_policies` is known as `panos_panorama_security_policy`.

This resource manages the full set of security rules, enforcing both the
contents of individual rules as well as their ordering.  Rules are defined in
a `rule` config block.  As this manages the full set of security rules for
a given rulebase, any extraneous rules are removed on `terraform apply`.

!> **Note**: This resource will remove any security rule not defined in your plan file.

For each security rule, there are three styles of profile settings:

* `None` (the default)
* `Group`
* `Profiles`

The Profile Setting is implicitly chosen based on what params are configured
for the security rule.  If you want a Profile Setting of `Group`, then the
`group` param should be set to the desired Group Profile.  If you want a
Profile Setting of `Profiles`, then you will need to specify one or more of
the following params:

* `virus`
* `spyware`
* `vulnerab...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Panos::PanoramaSecurityPolicy",
    "Properties" : {
        "<a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>" : <i>String</i>,
        "<a href="#rulebase" title="Rulebase">Rulebase</a>" : <i>String</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Panos::PanoramaSecurityPolicy
Properties:
    <a href="#devicegroup" title="DeviceGroup">DeviceGroup</a>: <i>String</i>
    <a href="#rulebase" title="Rulebase">Rulebase</a>: <i>String</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
</pre>

## Properties

#### DeviceGroup

The device group to put the security policy into
(default: `shared`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rulebase

The rulebase.  This can be `pre-rulebase` (default),
`post-rulebase`, or `rulebase`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

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


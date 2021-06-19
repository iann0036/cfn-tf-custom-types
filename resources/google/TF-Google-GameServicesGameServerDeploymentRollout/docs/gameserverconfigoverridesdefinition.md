# TF::Google::GameServicesGameServerDeploymentRollout GameServerConfigOverridesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#configversion" title="ConfigVersion">ConfigVersion</a>" : <i>String</i>,
    "<a href="#realmsselector" title="RealmsSelector">RealmsSelector</a>" : <i>[ <a href="realmsselectordefinition.md">RealmsSelectorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#configversion" title="ConfigVersion">ConfigVersion</a>: <i>String</i>
<a href="#realmsselector" title="RealmsSelector">RealmsSelector</a>: <i>
      - <a href="realmsselectordefinition.md">RealmsSelectorDefinition</a></i>
</pre>

## Properties

#### ConfigVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RealmsSelector

_Required_: No

_Type_: List of <a href="realmsselectordefinition.md">RealmsSelectorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


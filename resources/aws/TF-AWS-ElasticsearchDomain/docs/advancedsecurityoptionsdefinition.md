# TF::AWS::ElasticsearchDomain AdvancedSecurityOptionsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
    "<a href="#internaluserdatabaseenabled" title="InternalUserDatabaseEnabled">InternalUserDatabaseEnabled</a>" : <i>Boolean</i>,
    "<a href="#masteruseroptions" title="MasterUserOptions">MasterUserOptions</a>" : <i>[ <a href="masteruseroptionsdefinition.md">MasterUserOptionsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
<a href="#internaluserdatabaseenabled" title="InternalUserDatabaseEnabled">InternalUserDatabaseEnabled</a>: <i>Boolean</i>
<a href="#masteruseroptions" title="MasterUserOptions">MasterUserOptions</a>: <i>
      - <a href="masteruseroptionsdefinition.md">MasterUserOptionsDefinition</a></i>
</pre>

## Properties

#### Enabled

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalUserDatabaseEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterUserOptions

_Required_: No

_Type_: List of <a href="masteruseroptionsdefinition.md">MasterUserOptionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


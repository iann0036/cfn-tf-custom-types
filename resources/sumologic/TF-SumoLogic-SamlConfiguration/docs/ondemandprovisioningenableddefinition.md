# TF::SumoLogic::SamlConfiguration OnDemandProvisioningEnabledDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#firstnameattribute" title="FirstNameAttribute">FirstNameAttribute</a>" : <i>String</i>,
    "<a href="#lastnameattribute" title="LastNameAttribute">LastNameAttribute</a>" : <i>String</i>,
    "<a href="#ondemandprovisioningroles" title="OnDemandProvisioningRoles">OnDemandProvisioningRoles</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#firstnameattribute" title="FirstNameAttribute">FirstNameAttribute</a>: <i>String</i>
<a href="#lastnameattribute" title="LastNameAttribute">LastNameAttribute</a>: <i>String</i>
<a href="#ondemandprovisioningroles" title="OnDemandProvisioningRoles">OnDemandProvisioningRoles</a>: <i>
      - String</i>
</pre>

## Properties

#### FirstNameAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastNameAttribute

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OnDemandProvisioningRoles

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


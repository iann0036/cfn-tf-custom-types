# TF::Dome9::User IamSafeDefinition2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudaccountid" title="CloudAccountId">CloudAccountId</a>" : <i>String</i>,
    "<a href="#cloudaccountstate" title="CloudAccountState">CloudAccountState</a>" : <i>String</i>,
    "<a href="#externalaccountnumber" title="ExternalAccountNumber">ExternalAccountNumber</a>" : <i>String</i>,
    "<a href="#iamentities" title="IamEntities">IamEntities</a>" : <i>[ String, ... ]</i>,
    "<a href="#iamentitieslastleasetime" title="IamEntitiesLastLeaseTime">IamEntitiesLastLeaseTime</a>" : <i>[ <a href="iamsafedefinition.md">IamSafeDefinition</a>, ... ]</i>,
    "<a href="#iamentity" title="IamEntity">IamEntity</a>" : <i>String</i>,
    "<a href="#lastleasetime" title="LastLeaseTime">LastLeaseTime</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#state" title="State">State</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#cloudaccountid" title="CloudAccountId">CloudAccountId</a>: <i>String</i>
<a href="#cloudaccountstate" title="CloudAccountState">CloudAccountState</a>: <i>String</i>
<a href="#externalaccountnumber" title="ExternalAccountNumber">ExternalAccountNumber</a>: <i>String</i>
<a href="#iamentities" title="IamEntities">IamEntities</a>: <i>
      - String</i>
<a href="#iamentitieslastleasetime" title="IamEntitiesLastLeaseTime">IamEntitiesLastLeaseTime</a>: <i>
      - <a href="iamsafedefinition.md">IamSafeDefinition</a></i>
<a href="#iamentity" title="IamEntity">IamEntity</a>: <i>String</i>
<a href="#lastleasetime" title="LastLeaseTime">LastLeaseTime</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#state" title="State">State</a>: <i>Boolean</i>
</pre>

## Properties

#### CloudAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudAccountState

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalAccountNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamEntities

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamEntitiesLastLeaseTime

_Required_: No

_Type_: List of <a href="iamsafedefinition.md">IamSafeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IamEntity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastLeaseTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


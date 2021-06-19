# TF::AVI::Albservicesconfig AssetContactDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
    "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
    "<a href="#email" title="Email">Email</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#phone" title="Phone">Phone</a>" : <i>String</i>,
    "<a href="#managedaccounts" title="ManagedAccounts">ManagedAccounts</a>" : <i>[ <a href="managedaccountsdefinition.md">ManagedAccountsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
<a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
<a href="#email" title="Email">Email</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#phone" title="Phone">Phone</a>: <i>String</i>
<a href="#managedaccounts" title="ManagedAccounts">ManagedAccounts</a>: <i>
      - <a href="managedaccountsdefinition.md">ManagedAccountsDefinition</a></i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Phone

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManagedAccounts

_Required_: No

_Type_: List of <a href="managedaccountsdefinition.md">ManagedAccountsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


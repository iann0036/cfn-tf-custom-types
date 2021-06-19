# TF::CheckPoint::ManagementAccessRole UsersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#basedn" title="BaseDn">BaseDn</a>" : <i>String</i>,
    "<a href="#selection" title="Selection">Selection</a>" : <i>[ String, ... ]</i>,
    "<a href="#source" title="Source">Source</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#basedn" title="BaseDn">BaseDn</a>: <i>String</i>
<a href="#selection" title="Selection">Selection</a>: <i>
      - String</i>
<a href="#source" title="Source">Source</a>: <i>String</i>
</pre>

## Properties

#### BaseDn

When source is "Active Directory" use "base-dn" to refine the query in AD database.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Selection

Name or UID of an object selected from source.selection blocks are documented below.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

Active Directory name or UID or Identity Tag  or Internal User Groups or LDAP groups or Guests.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


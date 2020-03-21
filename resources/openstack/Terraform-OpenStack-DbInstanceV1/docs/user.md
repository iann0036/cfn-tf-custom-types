# Terraform::OpenStack::DbInstanceV1 User

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#databases" title="Databases">Databases</a>" : <i>[ String, ... ]</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#password" title="Password">Password</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#databases" title="Databases">Databases</a>: <i>
      - String</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#password" title="Password">Password</a>: <i>String</i>
</pre>

## Properties

#### Databases

A list of databases that user will have access to. If not specified,
user has access to all databases on th einstance. Changing this creates a new instance.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

An ip address or % sign indicating what ip addresses can connect with
this user credentials. Changing this creates a new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Username to be created on new instance. Changing this creates a
new instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

User's password. Changing this creates a
new instance.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


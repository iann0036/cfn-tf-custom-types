# TF::FortiOS::SystemAdminAdministrator

Provides a resource to configure administrator accounts of FortiOS.

!> **Warning:** The resource will be deprecated and replaced by new resource `fortios_system_admin`, we recommend that you use the new resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::SystemAdminAdministrator",
    "Properties" : {
        "<a href="#accprofile" title="Accprofile">Accprofile</a>" : <i>String</i>,
        "<a href="#comments" title="Comments">Comments</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#password" title="Password">Password</a>" : <i>String</i>,
        "<a href="#trusthost1" title="Trusthost1">Trusthost1</a>" : <i>String</i>,
        "<a href="#trusthost10" title="Trusthost10">Trusthost10</a>" : <i>String</i>,
        "<a href="#trusthost2" title="Trusthost2">Trusthost2</a>" : <i>String</i>,
        "<a href="#trusthost3" title="Trusthost3">Trusthost3</a>" : <i>String</i>,
        "<a href="#trusthost4" title="Trusthost4">Trusthost4</a>" : <i>String</i>,
        "<a href="#trusthost5" title="Trusthost5">Trusthost5</a>" : <i>String</i>,
        "<a href="#trusthost6" title="Trusthost6">Trusthost6</a>" : <i>String</i>,
        "<a href="#trusthost7" title="Trusthost7">Trusthost7</a>" : <i>String</i>,
        "<a href="#trusthost8" title="Trusthost8">Trusthost8</a>" : <i>String</i>,
        "<a href="#trusthost9" title="Trusthost9">Trusthost9</a>" : <i>String</i>,
        "<a href="#vdom" title="Vdom">Vdom</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::SystemAdminAdministrator
Properties:
    <a href="#accprofile" title="Accprofile">Accprofile</a>: <i>String</i>
    <a href="#comments" title="Comments">Comments</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#password" title="Password">Password</a>: <i>String</i>
    <a href="#trusthost1" title="Trusthost1">Trusthost1</a>: <i>String</i>
    <a href="#trusthost10" title="Trusthost10">Trusthost10</a>: <i>String</i>
    <a href="#trusthost2" title="Trusthost2">Trusthost2</a>: <i>String</i>
    <a href="#trusthost3" title="Trusthost3">Trusthost3</a>: <i>String</i>
    <a href="#trusthost4" title="Trusthost4">Trusthost4</a>: <i>String</i>
    <a href="#trusthost5" title="Trusthost5">Trusthost5</a>: <i>String</i>
    <a href="#trusthost6" title="Trusthost6">Trusthost6</a>: <i>String</i>
    <a href="#trusthost7" title="Trusthost7">Trusthost7</a>: <i>String</i>
    <a href="#trusthost8" title="Trusthost8">Trusthost8</a>: <i>String</i>
    <a href="#trusthost9" title="Trusthost9">Trusthost9</a>: <i>String</i>
    <a href="#vdom" title="Vdom">Vdom</a>: <i>
      - String</i>
</pre>

## Properties

#### Accprofile

Access profile for this administrator. Access profiles control administrator access to FortiGate features.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comments

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

User name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Password

Admin user password.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost1

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost10

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost2

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost3

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost4

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost5

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost6

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost7

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost8

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Trusthost9

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdom

Virtual domain(s) that the administrator can access.

_Required_: No

_Type_: List of String

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


# TF::NewRelic::OneDashboard

CloudFormation equivalent of newrelic_one_dashboard

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::OneDashboard",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#permissions" title="Permissions">Permissions</a>" : <i>String</i>,
        "<a href="#page" title="Page">Page</a>" : <i>[ <a href="pagedefinition.md">PageDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::OneDashboard
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#permissions" title="Permissions">Permissions</a>: <i>String</i>
    <a href="#page" title="Page">Page</a>: <i>
      - <a href="pagedefinition.md">PageDefinition</a></i>
</pre>

## Properties

#### AccountId

Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
* `description` - (Optional) Brief text describing the dashboard.
* `permissions` - (Optional) Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Brief text describing the dashboard.
* `permissions` - (Optional) Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of the dashboard.
* `page` - (Required) A nested block that describes a page. See [Nested page blocks](#nested-page-blocks) below for details.
* `account_id` - (Optional) Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
* `description` - (Optional) Brief text describing the dashboard.
* `permissions` - (Optional) Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Permissions

Determines who can see the dashboard in an account. Valid values are `private`, `public_read_only`, or `public_read_write`.  Defaults to `public_read_only`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Page

_Required_: No

_Type_: List of <a href="pagedefinition.md">PageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Guid

Returns the <code>Guid</code> value.

#### Id

Returns the <code>Id</code> value.

#### Permalink

Returns the <code>Permalink</code> value.


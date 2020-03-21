# Terraform::Scaleway::LbFrontendBeta Acl

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#organizationid" title="OrganizationId">OrganizationId</a>" : <i>String</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;acl-action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
    "<a href="#match" title="Match">Match</a>" : <i>[ &lt;a href=&#34;acl-match.md&#34;&gt;Match&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#organizationid" title="OrganizationId">OrganizationId</a>: <i>String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;acl-action.md&#34;&gt;Action&lt;/a&gt;</i>
<a href="#match" title="Match">Match</a>: <i>
      - &lt;a href=&#34;acl-match.md&#34;&gt;Match&lt;/a&gt;</i>
</pre>

## Properties

#### Name

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrganizationId

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No
_Type_: List of &lt;a href=&#34;acl-action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Match

_Required_: No
_Type_: List of &lt;a href=&#34;acl-match.md&#34;&gt;Match&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::AzureRM::ApiManagementBackend Credentials

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>[ String, ... ]</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ &lt;a href=&#34;credentials-header.md&#34;&gt;Header&lt;/a&gt;, ... ]</i>,
    "<a href="#query" title="Query">Query</a>" : <i>[ &lt;a href=&#34;credentials-query.md&#34;&gt;Query&lt;/a&gt;, ... ]</i>,
    "<a href="#authorization" title="Authorization">Authorization</a>" : <i>[ &lt;a href=&#34;credentials-authorization.md&#34;&gt;Authorization&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>
      - String</i>
<a href="#header" title="Header">Header</a>: <i>
      - &lt;a href=&#34;credentials-header.md&#34;&gt;Header&lt;/a&gt;</i>
<a href="#query" title="Query">Query</a>: <i>
      - &lt;a href=&#34;credentials-query.md&#34;&gt;Query&lt;/a&gt;</i>
<a href="#authorization" title="Authorization">Authorization</a>: <i>
      - &lt;a href=&#34;credentials-authorization.md&#34;&gt;Authorization&lt;/a&gt;</i>
</pre>

## Properties

#### Certificate

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No
_Type_: List of &lt;a href=&#34;credentials-header.md&#34;&gt;Header&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Query

_Required_: No
_Type_: List of &lt;a href=&#34;credentials-query.md&#34;&gt;Query&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Authorization

_Required_: No
_Type_: List of &lt;a href=&#34;credentials-authorization.md&#34;&gt;Authorization&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


# Terraform::OCI::DatabaseDbSystem DbHome

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#dbversion" title="DbVersion">DbVersion</a>" : <i>String</i>,
    "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
    "<a href="#database" title="Database">Database</a>" : <i>[ &lt;a href=&#34;dbhome-database.md&#34;&gt;Database&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#dbversion" title="DbVersion">DbVersion</a>: <i>String</i>
<a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
<a href="#database" title="Database">Database</a>: <i>
      - &lt;a href=&#34;dbhome-database.md&#34;&gt;Database&lt;/a&gt;</i>
</pre>

## Properties

#### DbVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Database

_Required_: No
_Type_: List of &lt;a href=&#34;dbhome-database.md&#34;&gt;Database&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


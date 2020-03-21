# Terraform::Nomad::QuotaSpecification Limits

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#regionlimit" title="RegionLimit">RegionLimit</a>" : <i>[ &lt;a href=&#34;limits-regionlimit.md&#34;&gt;RegionLimit&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#regionlimit" title="RegionLimit">RegionLimit</a>: <i>
      - &lt;a href=&#34;limits-regionlimit.md&#34;&gt;RegionLimit&lt;/a&gt;</i>
</pre>

## Properties

#### Region

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionLimit

_Required_: No
_Type_: List of &lt;a href=&#34;limits-regionlimit.md&#34;&gt;RegionLimit&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


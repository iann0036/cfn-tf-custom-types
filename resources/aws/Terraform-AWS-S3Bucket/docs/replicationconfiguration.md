# Terraform::AWS::S3Bucket ReplicationConfiguration

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#role" title="Role">Role</a>" : <i>String</i>,
    "<a href="#rules" title="Rules">Rules</a>" : <i>[ &lt;a href=&#34;replicationconfiguration-rules.md&#34;&gt;Rules&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#role" title="Role">Role</a>: <i>String</i>
<a href="#rules" title="Rules">Rules</a>: <i>
      - &lt;a href=&#34;replicationconfiguration-rules.md&#34;&gt;Rules&lt;/a&gt;</i>
</pre>

## Properties

#### Role

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rules

_Required_: No
_Type_: List of &lt;a href=&#34;replicationconfiguration-rules.md&#34;&gt;Rules&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


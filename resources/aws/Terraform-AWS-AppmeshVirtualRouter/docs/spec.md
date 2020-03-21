# Terraform::AWS::AppmeshVirtualRouter Spec

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servicenames" title="ServiceNames">ServiceNames</a>" : <i>[ String, ... ]</i>,
    "<a href="#listener" title="Listener">Listener</a>" : <i>[ &lt;a href=&#34;spec-listener.md&#34;&gt;Listener&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#servicenames" title="ServiceNames">ServiceNames</a>: <i>
      - String</i>
<a href="#listener" title="Listener">Listener</a>: <i>
      - &lt;a href=&#34;spec-listener.md&#34;&gt;Listener&lt;/a&gt;</i>
</pre>

## Properties

#### ServiceNames

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Listener

_Required_: No
_Type_: List of &lt;a href=&#34;spec-listener.md&#34;&gt;Listener&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


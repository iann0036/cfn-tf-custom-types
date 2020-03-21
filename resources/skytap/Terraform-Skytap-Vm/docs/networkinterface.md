# Terraform::Skytap::Vm NetworkInterface

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#interfacetype" title="InterfaceType">InterfaceType</a>" : <i>String</i>,
    "<a href="#ip" title="Ip">Ip</a>" : <i>String</i>,
    "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
    "<a href="#publishedservice" title="PublishedService">PublishedService</a>" : <i>[ &lt;a href=&#34;networkinterface-publishedservice.md&#34;&gt;PublishedService&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#interfacetype" title="InterfaceType">InterfaceType</a>: <i>String</i>
<a href="#ip" title="Ip">Ip</a>: <i>String</i>
<a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
<a href="#publishedservice" title="PublishedService">PublishedService</a>: <i>
      - &lt;a href=&#34;networkinterface-publishedservice.md&#34;&gt;PublishedService&lt;/a&gt;</i>
</pre>

## Properties

#### Hostname

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InterfaceType

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ip

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublishedService

_Required_: No
_Type_: List of &lt;a href=&#34;networkinterface-publishedservice.md&#34;&gt;PublishedService&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


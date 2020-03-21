# Terraform::Circonus::Check Consul

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#acltoken" title="AclToken">AclToken</a>" : <i>String</i>,
    "<a href="#allowstale" title="AllowStale">AllowStale</a>" : <i>Boolean</i>,
    "<a href="#cachain" title="CaChain">CaChain</a>" : <i>String</i>,
    "<a href="#certificatefile" title="CertificateFile">CertificateFile</a>" : <i>String</i>,
    "<a href="#checkblacklist" title="CheckBlacklist">CheckBlacklist</a>" : <i>[ String, ... ]</i>,
    "<a href="#ciphers" title="Ciphers">Ciphers</a>" : <i>String</i>,
    "<a href="#dc" title="Dc">Dc</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ &lt;a href=&#34;consul-headers.md&#34;&gt;Headers&lt;/a&gt;, ... ]</i>,
    "<a href="#httpaddr" title="HttpAddr">HttpAddr</a>" : <i>String</i>,
    "<a href="#keyfile" title="KeyFile">KeyFile</a>" : <i>String</i>,
    "<a href="#node" title="Node">Node</a>" : <i>String</i>,
    "<a href="#nodeblacklist" title="NodeBlacklist">NodeBlacklist</a>" : <i>[ String, ... ]</i>,
    "<a href="#service" title="Service">Service</a>" : <i>String</i>,
    "<a href="#serviceblacklist" title="ServiceBlacklist">ServiceBlacklist</a>" : <i>[ String, ... ]</i>,
    "<a href="#state" title="State">State</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#acltoken" title="AclToken">AclToken</a>: <i>String</i>
<a href="#allowstale" title="AllowStale">AllowStale</a>: <i>Boolean</i>
<a href="#cachain" title="CaChain">CaChain</a>: <i>String</i>
<a href="#certificatefile" title="CertificateFile">CertificateFile</a>: <i>String</i>
<a href="#checkblacklist" title="CheckBlacklist">CheckBlacklist</a>: <i>
      - String</i>
<a href="#ciphers" title="Ciphers">Ciphers</a>: <i>String</i>
<a href="#dc" title="Dc">Dc</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - &lt;a href=&#34;consul-headers.md&#34;&gt;Headers&lt;/a&gt;</i>
<a href="#httpaddr" title="HttpAddr">HttpAddr</a>: <i>String</i>
<a href="#keyfile" title="KeyFile">KeyFile</a>: <i>String</i>
<a href="#node" title="Node">Node</a>: <i>String</i>
<a href="#nodeblacklist" title="NodeBlacklist">NodeBlacklist</a>: <i>
      - String</i>
<a href="#service" title="Service">Service</a>: <i>String</i>
<a href="#serviceblacklist" title="ServiceBlacklist">ServiceBlacklist</a>: <i>
      - String</i>
<a href="#state" title="State">State</a>: <i>String</i>
</pre>

## Properties

#### AclToken

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowStale

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaChain

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateFile

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckBlacklist

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphers

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dc

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No
_Type_: List of &lt;a href=&#34;consul-headers.md&#34;&gt;Headers&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpAddr

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyFile

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Node

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeBlacklist

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Service

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceBlacklist

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


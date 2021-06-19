# TF::Circonus::Check JsonDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authmethod" title="AuthMethod">AuthMethod</a>" : <i>String</i>,
    "<a href="#authpassword" title="AuthPassword">AuthPassword</a>" : <i>String</i>,
    "<a href="#authuser" title="AuthUser">AuthUser</a>" : <i>String</i>,
    "<a href="#cachain" title="CaChain">CaChain</a>" : <i>String</i>,
    "<a href="#certificatefile" title="CertificateFile">CertificateFile</a>" : <i>String</i>,
    "<a href="#ciphers" title="Ciphers">Ciphers</a>" : <i>String</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>,
    "<a href="#keyfile" title="KeyFile">KeyFile</a>" : <i>String</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#payload" title="Payload">Payload</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#readlimit" title="ReadLimit">ReadLimit</a>" : <i>Double</i>,
    "<a href="#url" title="Url">Url</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#authmethod" title="AuthMethod">AuthMethod</a>: <i>String</i>
<a href="#authpassword" title="AuthPassword">AuthPassword</a>: <i>String</i>
<a href="#authuser" title="AuthUser">AuthUser</a>: <i>String</i>
<a href="#cachain" title="CaChain">CaChain</a>: <i>String</i>
<a href="#certificatefile" title="CertificateFile">CertificateFile</a>: <i>String</i>
<a href="#ciphers" title="Ciphers">Ciphers</a>: <i>String</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
<a href="#keyfile" title="KeyFile">KeyFile</a>: <i>String</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#payload" title="Payload">Payload</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#readlimit" title="ReadLimit">ReadLimit</a>: <i>Double</i>
<a href="#url" title="Url">Url</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
</pre>

## Properties

#### AuthMethod

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthPassword

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthUser

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaChain

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ciphers

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyFile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Payload

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReadLimit

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Url

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


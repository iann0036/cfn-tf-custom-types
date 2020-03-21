# Terraform::AzureRM::ApplicationGateway SslPolicy

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>" : <i>[ String, ... ]</i>,
    "<a href="#disabledprotocols" title="DisabledProtocols">DisabledProtocols</a>" : <i>[ String, ... ]</i>,
    "<a href="#minprotocolversion" title="MinProtocolVersion">MinProtocolVersion</a>" : <i>String</i>,
    "<a href="#policyname" title="PolicyName">PolicyName</a>" : <i>String</i>,
    "<a href="#policytype" title="PolicyType">PolicyType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#ciphersuites" title="CipherSuites">CipherSuites</a>: <i>
      - String</i>
<a href="#disabledprotocols" title="DisabledProtocols">DisabledProtocols</a>: <i>
      - String</i>
<a href="#minprotocolversion" title="MinProtocolVersion">MinProtocolVersion</a>: <i>String</i>
<a href="#policyname" title="PolicyName">PolicyName</a>: <i>String</i>
<a href="#policytype" title="PolicyType">PolicyType</a>: <i>String</i>
</pre>

## Properties

#### CipherSuites

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisabledProtocols

_Required_: No
_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinProtocolVersion

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyName

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyType

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


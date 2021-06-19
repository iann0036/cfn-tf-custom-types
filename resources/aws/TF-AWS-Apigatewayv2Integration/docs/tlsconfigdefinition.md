# TF::AWS::Apigatewayv2Integration TlsConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#servernametoverify" title="ServerNameToVerify">ServerNameToVerify</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#servernametoverify" title="ServerNameToVerify">ServerNameToVerify</a>: <i>String</i>
</pre>

## Properties

#### ServerNameToVerify

If you specify a server name, API Gateway uses it to verify the hostname on the integration's certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


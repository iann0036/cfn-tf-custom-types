# TF::FortiOS::FirewallProfileprotocoloptions ServerKeytabDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keytab" title="Keytab">Keytab</a>" : <i>String</i>,
    "<a href="#principal" title="Principal">Principal</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#keytab" title="Keytab">Keytab</a>: <i>String</i>
<a href="#principal" title="Principal">Principal</a>: <i>String</i>
</pre>

## Properties

#### Keytab

Base64 encoded keytab file containing credential of the server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Principal

Service principal.  For example, "host/cifsserver.example.com@example.com".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


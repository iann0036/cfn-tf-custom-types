# Terraform::Circonus::Check Snmp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#authpassphrase" title="AuthPassphrase">AuthPassphrase</a>" : <i>String</i>,
    "<a href="#authprotocol" title="AuthProtocol">AuthProtocol</a>" : <i>String</i>,
    "<a href="#community" title="Community">Community</a>" : <i>String</i>,
    "<a href="#contextengine" title="ContextEngine">ContextEngine</a>" : <i>String</i>,
    "<a href="#contextname" title="ContextName">ContextName</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#privacypassphrase" title="PrivacyPassphrase">PrivacyPassphrase</a>" : <i>String</i>,
    "<a href="#privacyprotocol" title="PrivacyProtocol">PrivacyProtocol</a>" : <i>String</i>,
    "<a href="#securityengine" title="SecurityEngine">SecurityEngine</a>" : <i>String</i>,
    "<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>" : <i>String</i>,
    "<a href="#securityname" title="SecurityName">SecurityName</a>" : <i>String</i>,
    "<a href="#separatequeries" title="SeparateQueries">SeparateQueries</a>" : <i>Boolean</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#oid" title="Oid">Oid</a>" : <i>[ <a href="snmp-oid.md">Oid</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#authpassphrase" title="AuthPassphrase">AuthPassphrase</a>: <i>String</i>
<a href="#authprotocol" title="AuthProtocol">AuthProtocol</a>: <i>String</i>
<a href="#community" title="Community">Community</a>: <i>String</i>
<a href="#contextengine" title="ContextEngine">ContextEngine</a>: <i>String</i>
<a href="#contextname" title="ContextName">ContextName</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#privacypassphrase" title="PrivacyPassphrase">PrivacyPassphrase</a>: <i>String</i>
<a href="#privacyprotocol" title="PrivacyProtocol">PrivacyProtocol</a>: <i>String</i>
<a href="#securityengine" title="SecurityEngine">SecurityEngine</a>: <i>String</i>
<a href="#securitylevel" title="SecurityLevel">SecurityLevel</a>: <i>String</i>
<a href="#securityname" title="SecurityName">SecurityName</a>: <i>String</i>
<a href="#separatequeries" title="SeparateQueries">SeparateQueries</a>: <i>Boolean</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#oid" title="Oid">Oid</a>: <i>
      - <a href="snmp-oid.md">Oid</a></i>
</pre>

## Properties

#### AuthPassphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Community

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContextEngine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContextName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivacyPassphrase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivacyProtocol

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityEngine

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityLevel

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeparateQueries

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Oid

_Required_: No

_Type_: List of <a href="snmp-oid.md">Oid</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


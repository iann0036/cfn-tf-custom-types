# TF::Volterra::HttpLoadbalancer HttpsAutoCertDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#addhsts" title="AddHsts">AddHsts</a>" : <i>Boolean</i>,
    "<a href="#appendservername" title="AppendServerName">AppendServerName</a>" : <i>String</i>,
    "<a href="#defaultheader" title="DefaultHeader">DefaultHeader</a>" : <i>Boolean</i>,
    "<a href="#httpredirect" title="HttpRedirect">HttpRedirect</a>" : <i>Boolean</i>,
    "<a href="#nomtls" title="NoMtls">NoMtls</a>" : <i>Boolean</i>,
    "<a href="#passthrough" title="PassThrough">PassThrough</a>" : <i>Boolean</i>,
    "<a href="#servername" title="ServerName">ServerName</a>" : <i>String</i>,
    "<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>" : <i>[ <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>, ... ]</i>,
    "<a href="#usemtls" title="UseMtls">UseMtls</a>" : <i>[ <a href="usemtlsdefinition.md">UseMtlsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#addhsts" title="AddHsts">AddHsts</a>: <i>Boolean</i>
<a href="#appendservername" title="AppendServerName">AppendServerName</a>: <i>String</i>
<a href="#defaultheader" title="DefaultHeader">DefaultHeader</a>: <i>Boolean</i>
<a href="#httpredirect" title="HttpRedirect">HttpRedirect</a>: <i>Boolean</i>
<a href="#nomtls" title="NoMtls">NoMtls</a>: <i>Boolean</i>
<a href="#passthrough" title="PassThrough">PassThrough</a>: <i>Boolean</i>
<a href="#servername" title="ServerName">ServerName</a>: <i>String</i>
<a href="#tlsconfig" title="TlsConfig">TlsConfig</a>: <i>
      - <a href="tlsconfigdefinition.md">TlsConfigDefinition</a></i>
<a href="#usemtls" title="UseMtls">UseMtls</a>: <i>
      - <a href="usemtlsdefinition.md">UseMtlsDefinition</a></i>
</pre>

## Properties

#### AddHsts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AppendServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultHeader

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpRedirect

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoMtls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PassThrough

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsConfig

_Required_: No

_Type_: List of <a href="tlsconfigdefinition.md">TlsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseMtls

_Required_: No

_Type_: List of <a href="usemtlsdefinition.md">UseMtlsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)


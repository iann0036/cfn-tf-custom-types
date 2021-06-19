# TF::Thunder::SlbTemplateSmtp

`thunder_slb_template_smtp` Provides details about thunder slb template smtp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::SlbTemplateSmtp",
    "Properties" : {
        "<a href="#clientstarttlstype" title="ClientStarttlsType">ClientStarttlsType</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#serverdomain" title="ServerDomain">ServerDomain</a>" : <i>String</i>,
        "<a href="#serverstarttlstype" title="ServerStarttlsType">ServerStarttlsType</a>" : <i>String</i>,
        "<a href="#servicereadymsg" title="ServiceReadyMsg">ServiceReadyMsg</a>" : <i>String</i>,
        "<a href="#usertag" title="UserTag">UserTag</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#clientdomainswitching" title="ClientDomainSwitching">ClientDomainSwitching</a>" : <i>[ <a href="clientdomainswitchingdefinition.md">ClientDomainSwitchingDefinition</a>, ... ]</i>,
        "<a href="#commanddisable" title="CommandDisable">CommandDisable</a>" : <i>[ <a href="commanddisabledefinition.md">CommandDisableDefinition</a>, ... ]</i>,
        "<a href="#template" title="Template">Template</a>" : <i>[ <a href="templatedefinition.md">TemplateDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::SlbTemplateSmtp
Properties:
    <a href="#clientstarttlstype" title="ClientStarttlsType">ClientStarttlsType</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#serverdomain" title="ServerDomain">ServerDomain</a>: <i>String</i>
    <a href="#serverstarttlstype" title="ServerStarttlsType">ServerStarttlsType</a>: <i>String</i>
    <a href="#servicereadymsg" title="ServiceReadyMsg">ServiceReadyMsg</a>: <i>String</i>
    <a href="#usertag" title="UserTag">UserTag</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#clientdomainswitching" title="ClientDomainSwitching">ClientDomainSwitching</a>: <i>
      - <a href="clientdomainswitchingdefinition.md">ClientDomainSwitchingDefinition</a></i>
    <a href="#commanddisable" title="CommandDisable">CommandDisable</a>: <i>
      - <a href="commanddisabledefinition.md">CommandDisableDefinition</a></i>
    <a href="#template" title="Template">Template</a>: <i>
      - <a href="templatedefinition.md">TemplateDefinition</a></i>
</pre>

## Properties

#### ClientStarttlsType

‘optional’: STARTTLS is optional requirement; ‘enforced’: Must issue STARTTLS command before mail transaction;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

SMTP Template Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerDomain

Config the domain of the email servers (Server’s domain, default is “mail-server-domain”).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerStarttlsType

‘optional’: STARTTLS is optional requirement; ‘enforced’: Must issue STARTTLS command before mail transaction;.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceReadyMsg

Set SMTP service ready message (SMTP service ready message, default is “ESMTP mail service ready”).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserTag

Customized tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClientDomainSwitching

_Required_: No

_Type_: List of <a href="clientdomainswitchingdefinition.md">ClientDomainSwitchingDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CommandDisable

_Required_: No

_Type_: List of <a href="commanddisabledefinition.md">CommandDisableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Template

_Required_: No

_Type_: List of <a href="templatedefinition.md">TemplateDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.


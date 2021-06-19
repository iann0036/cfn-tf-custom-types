# TF::Lacework::AlertChannelQradar

You can configure an alert channel to send Lacework alert notifications to IBM QRadar.

To find more information about the IBM QRadar alert channel integration, see the [Lacework support documentation](https://support.lacework.com/hc/en-us/articles/360056898693-IBM-QRadar).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::AlertChannelQradar",
    "Properties" : {
        "<a href="#communicationtype" title="CommunicationType">CommunicationType</a>" : <i>String</i>,
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#hostport" title="HostPort">HostPort</a>" : <i>Double</i>,
        "<a href="#hosturl" title="HostUrl">HostUrl</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::AlertChannelQradar
Properties:
    <a href="#communicationtype" title="CommunicationType">CommunicationType</a>: <i>String</i>
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#hostport" title="HostPort">HostPort</a>: <i>Double</i>
    <a href="#hosturl" title="HostUrl">HostUrl</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### CommunicationType

The communication protocol used. Must be one of `HTTPS` or `HTTPS Self Signed Cert`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostPort

The listen port defined in QRadar.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostUrl

The domain name or IP address of QRadar.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The Alert Channel integration name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.


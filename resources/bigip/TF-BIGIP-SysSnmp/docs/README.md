# TF::BIGIP::SysSnmp

`bigip_sys_snmp` provides details bout how to enable "ilx", "asm" "apm" resource on BIG-IP

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::SysSnmp",
    "Properties" : {
        "<a href="#allowedaddresses" title="Allowedaddresses">Allowedaddresses</a>" : <i>[ String, ... ]</i>,
        "<a href="#syscontact" title="SysContact">SysContact</a>" : <i>String</i>,
        "<a href="#syslocation" title="SysLocation">SysLocation</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::SysSnmp
Properties:
    <a href="#allowedaddresses" title="Allowedaddresses">Allowedaddresses</a>: <i>
      - String</i>
    <a href="#syscontact" title="SysContact">SysContact</a>: <i>String</i>
    <a href="#syslocation" title="SysLocation">SysLocation</a>: <i>String</i>
</pre>

## Properties

#### Allowedaddresses

Configures hosts or networks from which snmpd can accept traffic. Entries go directly into hosts.allow.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysContact

Specifies the contact information for the system administrator.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysLocation

Describes the system's physical location.

_Required_: No

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

#### Id

Returns the <code>Id</code> value.


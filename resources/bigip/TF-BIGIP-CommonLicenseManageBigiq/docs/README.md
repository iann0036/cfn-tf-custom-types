# TF::BIGIP::CommonLicenseManageBigiq

`bigip_common_license_manage_bigiq` This Resource is used for BIGIP/Provider License Management from BIGIQ

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::CommonLicenseManageBigiq",
    "Properties" : {
        "<a href="#assignmenttype" title="AssignmentType">AssignmentType</a>" : <i>String</i>,
        "<a href="#bigiqaddress" title="BigiqAddress">BigiqAddress</a>" : <i>String</i>,
        "<a href="#bigiqloginref" title="BigiqLoginRef">BigiqLoginRef</a>" : <i>String</i>,
        "<a href="#bigiqpassword" title="BigiqPassword">BigiqPassword</a>" : <i>String</i>,
        "<a href="#bigiqport" title="BigiqPort">BigiqPort</a>" : <i>String</i>,
        "<a href="#bigiqtokenauth" title="BigiqTokenAuth">BigiqTokenAuth</a>" : <i>Boolean</i>,
        "<a href="#bigiquser" title="BigiqUser">BigiqUser</a>" : <i>String</i>,
        "<a href="#devicelicensestatus" title="DeviceLicenseStatus">DeviceLicenseStatus</a>" : <i>String</i>,
        "<a href="#hypervisor" title="Hypervisor">Hypervisor</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#licensepoolname" title="LicensePoolname">LicensePoolname</a>" : <i>String</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#skukeyword1" title="Skukeyword1">Skukeyword1</a>" : <i>String</i>,
        "<a href="#skukeyword2" title="Skukeyword2">Skukeyword2</a>" : <i>String</i>,
        "<a href="#tenant" title="Tenant">Tenant</a>" : <i>String</i>,
        "<a href="#unitofmeasure" title="UnitOfMeasure">UnitOfMeasure</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::CommonLicenseManageBigiq
Properties:
    <a href="#assignmenttype" title="AssignmentType">AssignmentType</a>: <i>String</i>
    <a href="#bigiqaddress" title="BigiqAddress">BigiqAddress</a>: <i>String</i>
    <a href="#bigiqloginref" title="BigiqLoginRef">BigiqLoginRef</a>: <i>String</i>
    <a href="#bigiqpassword" title="BigiqPassword">BigiqPassword</a>: <i>String</i>
    <a href="#bigiqport" title="BigiqPort">BigiqPort</a>: <i>String</i>
    <a href="#bigiqtokenauth" title="BigiqTokenAuth">BigiqTokenAuth</a>: <i>Boolean</i>
    <a href="#bigiquser" title="BigiqUser">BigiqUser</a>: <i>String</i>
    <a href="#devicelicensestatus" title="DeviceLicenseStatus">DeviceLicenseStatus</a>: <i>String</i>
    <a href="#hypervisor" title="Hypervisor">Hypervisor</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#licensepoolname" title="LicensePoolname">LicensePoolname</a>: <i>String</i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#skukeyword1" title="Skukeyword1">Skukeyword1</a>: <i>String</i>
    <a href="#skukeyword2" title="Skukeyword2">Skukeyword2</a>: <i>String</i>
    <a href="#tenant" title="Tenant">Tenant</a>: <i>String</i>
    <a href="#unitofmeasure" title="UnitOfMeasure">UnitOfMeasure</a>: <i>String</i>
</pre>

## Properties

#### AssignmentType

The type of assignment, which is determined by whether the BIG-IP is unreachable, unmanaged, or managed by BIG-IQ. Possible values: “UNREACHABLE”, “UNMANAGED”, or “MANAGED”.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqAddress

BIGIQ License Manager IP Address, variable type `string`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqLoginRef

BIGIQ Login reference for token authentication.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqPassword

BIGIQ License Manager password.  variable type `string`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqPort

type `int`, BIGIQ License Manager Port number, specify if port is other than `443`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqTokenAuth

type `bool`, if set to `true` enables Token based Authentication,default is `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BigiqUser

BIGIQ License Manager username, variable type `string`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceLicenseStatus

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hypervisor

Identifies the platform running the BIG-IP VE. Possible values: “aws”, “azure”, “gce”, “vmware”, “hyperv”, “kvm”, or “xen”. type `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

License Assignment is done with specified `key`, supported only with RegKeypool type License assignement. type `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LicensePoolname

A name given to the license pool. type `string`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

MAC address of the BIG-IP. type `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Skukeyword1

An optional offering name. type `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Skukeyword2

An optional offering name. type `string`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenant

For an unreachable BIG-IP, you can provide an optional description for the assignment in this field.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UnitOfMeasure

The units used to measure billing. For example, “hourly” or “daily”. Type `string`.

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


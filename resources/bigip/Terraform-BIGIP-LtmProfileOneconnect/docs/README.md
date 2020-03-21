# Terraform::BIGIP::LtmProfileOneconnect

`bigip_ltm_profile_oneconnect` Configures a custom profile_oneconnect for use by health checks.

For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::BIGIP::LtmProfileOneconnect",
    "Properties" : {
        "<a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>" : <i>String</i>,
        "<a href="#idletimeoutoverride" title="IdleTimeoutOverride">IdleTimeoutOverride</a>" : <i>String</i>,
        "<a href="#maxage" title="MaxAge">MaxAge</a>" : <i>Double</i>,
        "<a href="#maxreuse" title="MaxReuse">MaxReuse</a>" : <i>Double</i>,
        "<a href="#maxsize" title="MaxSize">MaxSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#partition" title="Partition">Partition</a>" : <i>String</i>,
        "<a href="#sharepools" title="SharePools">SharePools</a>" : <i>String</i>,
        "<a href="#sourcemask" title="SourceMask">SourceMask</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::BIGIP::LtmProfileOneconnect
Properties:
    <a href="#defaultsfrom" title="DefaultsFrom">DefaultsFrom</a>: <i>String</i>
    <a href="#idletimeoutoverride" title="IdleTimeoutOverride">IdleTimeoutOverride</a>: <i>String</i>
    <a href="#maxage" title="MaxAge">MaxAge</a>: <i>Double</i>
    <a href="#maxreuse" title="MaxReuse">MaxReuse</a>: <i>Double</i>
    <a href="#maxsize" title="MaxSize">MaxSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#partition" title="Partition">Partition</a>: <i>String</i>
    <a href="#sharepools" title="SharePools">SharePools</a>: <i>String</i>
    <a href="#sourcemask" title="SourceMask">SourceMask</a>: <i>String</i>
</pre>

## Properties

#### DefaultsFrom

Specifies the profile that you want to use as the parent profile. Your new profile inherits all settings and values from the parent profile specified.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdleTimeoutOverride

Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion. Possible values are disabled, indefinite, or a numeric value that you specify. The default value is disabled.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxAge

Specifies the maximum age in number of seconds allowed for a connection in the connection reuse pool. For any connection with an age higher than this value, the system removes that connection from the reuse pool. The default value is 86400.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxReuse

Specifies the maximum number of times that a server-side connection can be reused. The default value is 1000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxSize

Specifies the maximum number of connections that the system holds in the connection reuse pool. If the pool is already full, then the server-side connection closes after the response is completed. The default value is 10000.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Partition

Displays the administrative partition within which this profile resides.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharePools

Specify if you want to share the pool, default value is "disabled".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceMask

Specifies a source IP mask. The default value is 0.0.0.0. The system applies the value of this option to the source address to determine its eligibility for reuse. A mask of 0.0.0.0 causes the system to share reused connections across all clients. A host mask (all 1's in binary), causes the system to share only those reused connections originating from the same client IP address.

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

